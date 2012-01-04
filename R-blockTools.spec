%global packname  blockTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Block, assign, and diagnose potential interference in randomized experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-gtools R-nbpMatching R-xtable 

BuildRequires:    R-devel tex(latex) R-MASS R-gtools R-nbpMatching R-xtable 

%description
Blocks units into experimental blocks, with one unit per treatment
condition, by creating a measure of multivariate distance between all
possible pairs of units.  Maximum, minimum, or an allowable range of
differences between units on one variable can be set.  Randomly assign
units to treatment conditions.  Diagnose potential interference between
units assigned to different treatment conditions.  Write outputs to .tex
and .csv files.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.3-1
- initial package for Fedora