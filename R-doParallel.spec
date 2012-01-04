%global packname  doParallel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Foreach parallel adaptor for the multicore package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreach R-iterators R-utils R-parallel 


BuildRequires:    R-devel tex(latex) R-foreach R-iterators R-utils R-parallel



%description
Provides a parallel backend for the %dopar% function using the parallel

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
%doc %{rlibdir}/doParallel/DESCRIPTION
%doc %{rlibdir}/doParallel/doc
%doc %{rlibdir}/doParallel/html
%{rlibdir}/doParallel/unitTests
%{rlibdir}/doParallel/examples
%{rlibdir}/doParallel/Meta
%{rlibdir}/doParallel/demo
%{rlibdir}/doParallel/NAMESPACE
%{rlibdir}/doParallel/R
%{rlibdir}/doParallel/INDEX
%{rlibdir}/doParallel/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora