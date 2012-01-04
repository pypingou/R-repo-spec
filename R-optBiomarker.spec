%global packname  optBiomarker
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.21
Release:          1%{?dist}
Summary:          Estimation of optimal number of biomarkers for two-group microarray based classifications at a given error tolerance level for various classification rules

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-21.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rpanel R-rgl 
Requires:         R-rgl R-MASS R-randomForest R-e1071 R-ipred R-msm 

BuildRequires:    R-devel tex(latex) R-rpanel R-rgl
BuildRequires:    R-rgl R-MASS R-randomForest R-e1071 R-ipred R-msm 


%description
Estimates optimal number of biomarkers for two-group classification based
on microarray data

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.21-1
- initial package for Fedora