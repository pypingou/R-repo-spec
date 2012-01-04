%global packname  rbenchmark
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Benchmarking routine for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
rbenchmark is inspired by the Perl module Benchmark, and is intended to
facilitate benchmarking of arbitrary R code. The library consists of just
one function, benchmark, which is a simple wrapper around system.time. 
Given a specification of the benchmarking process (counts of replications,
evaluation environment) and an arbitrary number of expressions, benchmark
evaluates each of the expressions in the specified environment,
replicating the evaluation as many times as specified, and returning the
results conveniently wrapped into a data frame.

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
%doc %{rlibdir}/rbenchmark/DESCRIPTION
%doc %{rlibdir}/rbenchmark/html
%{rlibdir}/rbenchmark/NAMESPACE
%{rlibdir}/rbenchmark/help
%{rlibdir}/rbenchmark/Meta
%{rlibdir}/rbenchmark/R
%{rlibdir}/rbenchmark/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora