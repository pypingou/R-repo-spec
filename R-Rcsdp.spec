%global packname  Rcsdp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.41
Release:          1%{?dist}
Summary:          R interface to the CSDP semidefinite programming library

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-41.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R interface to the CSDP semidefinite programming library. Installs version
6.0.1 of CSDP from the COIN-OR website if required. An existing
intallation of CSDP may be used by passing the proper configure arguments
to the installation command. See the INSTALL file for further details.

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
%doc %{rlibdir}/Rcsdp/DESCRIPTION
%doc %{rlibdir}/Rcsdp/html
%{rlibdir}/Rcsdp/INSTALL
%{rlibdir}/Rcsdp/libs
%{rlibdir}/Rcsdp/help
%{rlibdir}/Rcsdp/NAMESPACE
%{rlibdir}/Rcsdp/Meta
%{rlibdir}/Rcsdp/INDEX
%{rlibdir}/Rcsdp/LICENSE
%{rlibdir}/Rcsdp/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.41-1
- initial package for Fedora