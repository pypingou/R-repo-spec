%global packname  optimbase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          R port of the Scilab optimbase module

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Provides a set of commands to manage an abstract optimization method. The
goal is to provide a building block for a large class of specialized
optimization methods. This package manages: the number of variables, the
minimum and maximum bounds, the number of non linear inequality
constraints, the cost function, the logging system, various termination
criteria, etc...

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
%doc %{rlibdir}/optimbase/doc
%doc %{rlibdir}/optimbase/html
%doc %{rlibdir}/optimbase/DESCRIPTION
%{rlibdir}/optimbase/NAMESPACE
%{rlibdir}/optimbase/R
%{rlibdir}/optimbase/help
%{rlibdir}/optimbase/INDEX
%{rlibdir}/optimbase/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora