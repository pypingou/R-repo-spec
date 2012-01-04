%global packname  weights
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.70
Release:          1%{?dist}
Summary:          Weighting and Weighted Statistics

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-anesrake R-gdata 


BuildRequires:    R-devel tex(latex) R-Hmisc R-anesrake R-gdata



%description
This package currently provides a variety of functions for producing
simple weighted statistics are also included, such as weighted histograms,
Pearson's correlations, partial correlations, Chi-Squareds, and t-tests. 
Also now includes some software for quickly recoding survey data.  Future
versions of the package will be more closely integrated with anesrake and
additional weighting tools and will provide the option to find weighting
benchmarks and weight data using a variety of methodologies.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.70-1
- initial package for Fedora