%global packname  nloptr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.8
Release:          1%{?dist}
Summary:          R interface to NLopt

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
nloptr is an R interface to NLopt. NLopt is a free/open-source library for
nonlinear optimization, providing a common interface for a number of
different free optimization routines available online as well as original
implementations of various other algorithms. See
http://ab-initio.mit.edu/wiki/index.php/NLopt_Introduction for more
information on the available algorithms.

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
%doc %{rlibdir}/nloptr/DESCRIPTION
%doc %{rlibdir}/nloptr/CITATION
%doc %{rlibdir}/nloptr/html
%doc %{rlibdir}/nloptr/doc
%{rlibdir}/nloptr/data
%{rlibdir}/nloptr/libs
%{rlibdir}/nloptr/LICENSE
%{rlibdir}/nloptr/Meta
%{rlibdir}/nloptr/NAMESPACE
%{rlibdir}/nloptr/R
%{rlibdir}/nloptr/INDEX
%{rlibdir}/nloptr/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.8-1
- initial package for Fedora