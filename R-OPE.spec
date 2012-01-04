%global packname  OPE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Outer-product emulator

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Fit an outer-product emlator to the multivariate evaluations of a computer

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
%doc %{rlibdir}/OPE/DESCRIPTION
%doc %{rlibdir}/OPE/html
%{rlibdir}/OPE/INDEX
%{rlibdir}/OPE/R
%{rlibdir}/OPE/NAMESPACE
%{rlibdir}/OPE/help
%{rlibdir}/OPE/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora