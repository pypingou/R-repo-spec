%global packname  Rsymphony
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.12
Release:          1%{?dist}
Summary:          Symphony in R

Group:            Applications/Engineering 
License:          CPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R interface to the SYMPHONY MILP solver (version 5.2.4).

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
%doc %{rlibdir}/Rsymphony/html
%doc %{rlibdir}/Rsymphony/DESCRIPTION
%{rlibdir}/Rsymphony/Meta
%{rlibdir}/Rsymphony/libs
%{rlibdir}/Rsymphony/R
%{rlibdir}/Rsymphony/help
%{rlibdir}/Rsymphony/NAMESPACE
%{rlibdir}/Rsymphony/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.12-1
- initial package for Fedora