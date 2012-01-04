%global packname  foreach
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Foreach looping construct for R

Group:            Applications/Engineering 
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-iterators R-codetools R-utils 

BuildRequires:    R-devel tex(latex) R-iterators R-codetools R-utils 

%description
Support for the foreach looping construct.  Foreach is an idiom that
allows for iterating over elements in a collection, without the use of an
explicit loop counter.  This package in particular is intended to be used
for its return value, rather than for its side effects.  In that sense, it
is similar to the standard lapply function, but doesn't require the
evaluation of a function.  Using foreach without side effects also
facilitates executing the loop in parallel.

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
%doc %{rlibdir}/foreach/doc
%doc %{rlibdir}/foreach/html
%doc %{rlibdir}/foreach/DESCRIPTION
%{rlibdir}/foreach/examples
%{rlibdir}/foreach/Meta
%{rlibdir}/foreach/unitTests
%{rlibdir}/foreach/demo
%{rlibdir}/foreach/R
%{rlibdir}/foreach/NAMESPACE
%{rlibdir}/foreach/INDEX
RPM build errors:
%{rlibdir}/foreach/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora