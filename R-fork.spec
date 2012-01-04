%global packname  fork
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          R functions for handling multiple processes.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
These functions provides simple wrappers around the Unix process
management API calls: fork, signal, wait, waitpid, kill, and _exit.  This
enables construction of programs that utilize and mange multiple
concurrent processes.

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
%doc %{rlibdir}/fork/NEWS
%doc %{rlibdir}/fork/html
%doc %{rlibdir}/fork/DESCRIPTION
%{rlibdir}/fork/INDEX
%{rlibdir}/fork/R
%{rlibdir}/fork/NAMESPACE
%{rlibdir}/fork/ChangeLog
%{rlibdir}/fork/libs
%{rlibdir}/fork/Meta
%{rlibdir}/fork/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora