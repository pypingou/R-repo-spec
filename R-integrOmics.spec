%global packname  integrOmics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.55
Release:          1%{?dist}
Summary:          end of integrOmics package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
the integrOmics package is superseded by the mixOmics package

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/integrOmics/DESCRIPTION
%doc %{rlibdir}/integrOmics/html
%{rlibdir}/integrOmics/INDEX
%{rlibdir}/integrOmics/Meta
%{rlibdir}/integrOmics/R
%{rlibdir}/integrOmics/NAMESPACE
%{rlibdir}/integrOmics/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.55-1
- initial package for Fedora