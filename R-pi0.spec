%global packname  pi0
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.190
Release:          1%{?dist}
Summary:          Estimating the proportion of true null hypotheses for FDR

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-190.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-LowRankQP 
Requires:         R-Matrix R-numDeriv R-limSolve R-rgl R-scatterplot3d R-qvalue R-Iso R-quadprog R-kernlab 

BuildRequires:    R-devel tex(latex) R-LowRankQP
BuildRequires:    R-Matrix R-numDeriv R-limSolve R-rgl R-scatterplot3d R-qvalue R-Iso R-quadprog R-kernlab 


%description
This package implements method(s) to (approximately unbiasedly) estimate
the proportion of true null hypotheses, i.e., the pi0, when a very large
number of hypotheses are simultaneously tested, especially for the purpose
of (local) false discovery rate control for microarray data. It also
contains functions to estimate the distribution of noncentrality
parameters from a large number of parametric tests.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.190-1
- initial package for Fedora