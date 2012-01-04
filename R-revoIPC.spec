%global packname  revoIPC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Shared memory parallel framework for multicore machines

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package provides a fast parallel framework for multicore machines.

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
%doc %{rlibdir}/revoIPC/DESCRIPTION
%doc %{rlibdir}/revoIPC/html
%{rlibdir}/revoIPC/libs
%{rlibdir}/revoIPC/examples
%{rlibdir}/revoIPC/Meta
%{rlibdir}/revoIPC/help
%{rlibdir}/revoIPC/NAMESPACE
%{rlibdir}/revoIPC/INDEX
%{rlibdir}/revoIPC/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora