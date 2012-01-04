%global packname  batch
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Batching Routines in Parallel and Passing Command-Line Arguments to R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to allow you to easily pass command-line arguments into R, and
functions to aid in submitting your R code in parallel on a cluster and
joining the results afterward (e.g. multiple parameter values for
simulations running in parallel, splitting up a permutation test in
parallel, etc.). See `parseCommandArgs(...)' for the main example of how
to use this package.

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
%doc %{rlibdir}/batch/CITATION
%doc %{rlibdir}/batch/DESCRIPTION
%doc %{rlibdir}/batch/html
%{rlibdir}/batch/NAMESPACE
%{rlibdir}/batch/help
%{rlibdir}/batch/INDEX
%{rlibdir}/batch/R
%{rlibdir}/batch/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora