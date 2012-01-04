%global packname  MIPHENO
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Mutant Identification through Phenotypic High throughput Enabled NOrmalization

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-doBy R-gdata 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-doBy R-gdata 


%description
This package contains functions to carry out processing of high throughput
data analysis and detection of putative hits/mutants. Contents include a
function for post-hoc quality control for removal of outlier sample sets,
a median-based normalization method for use in datasets where there are no
explicit controls and where most of the responses are of the wildtype/no
response class (see accompanying paper). The package also includes a way
to prioritize individuals of interest using am empirical cumulative
distribution function. Methods for generating synthetic data as well as
data from the Chloroplast 2010 project are included.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora