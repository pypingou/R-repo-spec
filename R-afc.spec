%global packname  afc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Calculate afc

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package to calculate the Generalized Discrimination Score (also known as
Two Alternatives Forced Choice Score (2AFC)

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
%doc %{rlibdir}/afc/html
%doc %{rlibdir}/afc/DESCRIPTION
%{rlibdir}/afc/help
%{rlibdir}/afc/R
%{rlibdir}/afc/data
%{rlibdir}/afc/INDEX
%{rlibdir}/afc/NAMESPACE
%{rlibdir}/afc/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora