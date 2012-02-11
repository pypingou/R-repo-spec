%global packname  NMF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.09
Release:          1%{dist}
Summary:          Algorithms and framework for Nonnegative Matrix Factorization (NMF).

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-graphics 
Requires:         R-digest R-gridBase R-stringr R-colorspace
BuildRequires:    R-devel tex(latex) R-methods R-stats R-graphics 
BuildRequires:    R-digest R-gridBase R-stringr R-colorspace

%description
This package provides a framework to perform Non-negative Matrix
Factorization (NMF). It implements a set of already published algorithms
and seeding methods, and provides a framework to test, develop and plug
new/custom algorithms. Most of the built-in algorithms have been optimized
in C++, and the main interface function provides an easy way of performing
parallel computations on multicore machines.

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
%doc %{rlibdir}/NMF/DESCRIPTION
%doc %{rlibdir}/NMF/doc
%doc %{rlibdir}/NMF/CITATION
%doc %{rlibdir}/NMF/html
%doc %{rlibdir}/NMF/NEWS
%{rlibdir}/NMF/R
%{rlibdir}/NMF/libs
%{rlibdir}/NMF/INDEX
%{rlibdir}/NMF/matlab
%{rlibdir}/NMF/NAMESPACE
%{rlibdir}/NMF/help
%{rlibdir}/NMF/data
%{rlibdir}/NMF/Meta

%changelog
* Sat Feb 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.09-1
- Update to version 0.6.09

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.05-1
- initial package for Fedora
