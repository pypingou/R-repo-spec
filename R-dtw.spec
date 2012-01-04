%global packname  dtw
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.3
Release:          1%{?dist}
Summary:          Dynamic Time Warping algorithms

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.14-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-proxy 

BuildRequires:    R-devel tex(latex) R-methods R-proxy 

%description
Comprehensive implementation of Dynamic Time Warping algorithms in R. DTW
finds the optimal (least cumulative distance) mapping between two time
series.  All common DTW variants are covered, including local and global
constraints, arbitrary timeseries lenghts, distance definitions, MVM, etc.
Package computes cumulative distance, warping functions, plots,
normalizations, etc.

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
%doc %{rlibdir}/dtw/html
%doc %{rlibdir}/dtw/doc
%doc %{rlibdir}/dtw/CITATION
%doc %{rlibdir}/dtw/DESCRIPTION
%{rlibdir}/dtw/demo
%{rlibdir}/dtw/TODO
%{rlibdir}/dtw/libs
%{rlibdir}/dtw/data
%{rlibdir}/dtw/Meta
%{rlibdir}/dtw/ChangeLog
%{rlibdir}/dtw/help
%{rlibdir}/dtw/R
%{rlibdir}/dtw/INDEX
%{rlibdir}/dtw/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.3-1
- initial package for Fedora