%global packname  odesolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.20
Release:          1%{?dist}
Summary:          Solvers for Ordinary Differential Equations

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides an interface for the ODE solver lsoda. ODEs are
expressed as R functions or as compiled code. This is deprecated!  Use
deSolve instead.

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
%doc %{rlibdir}/odesolve/DESCRIPTION
%doc %{rlibdir}/odesolve/html
%{rlibdir}/odesolve/help
%{rlibdir}/odesolve/NAMESPACE
%{rlibdir}/odesolve/data
%{rlibdir}/odesolve/demo
%{rlibdir}/odesolve/dynload
%{rlibdir}/odesolve/libs
%{rlibdir}/odesolve/Meta
%{rlibdir}/odesolve/R
%{rlibdir}/odesolve/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.20-1
- initial package for Fedora