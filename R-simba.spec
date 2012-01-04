%global packname  simba
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          A Collection of functions for similarity analysis of vegetation data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-vegan 


BuildRequires:    R-devel tex(latex) R-stats R-vegan



%description
Besides functions for the calculation of similarity and multiple plot
similarity measures with binary data (for instance presence/absence
species data) the package contains some simple wrapper functions for
reshaping species lists into matrices and vice versa and some other
functions for further processing of similarity data (Mantel-like
permutation procedures) as well as some other useful stuff for vegetation

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora