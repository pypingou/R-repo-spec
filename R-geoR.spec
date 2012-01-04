%global packname  geoR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Analysis of geostatistical data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-sp R-methods R-MASS 
Requires:         R-splancs R-RandomFields 

BuildRequires:    R-devel tex(latex) R-stats R-sp R-methods R-MASS
BuildRequires:    R-splancs R-RandomFields 


%description
Geostatistical analysis including traditional, likelihood-based and
Bayesian methods.

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
%doc %{rlibdir}/geoR/CITATION
%doc %{rlibdir}/geoR/html
%doc %{rlibdir}/geoR/doc
%doc %{rlibdir}/geoR/DESCRIPTION
%{rlibdir}/geoR/R
%{rlibdir}/geoR/CHANGES
%{rlibdir}/geoR/help
%{rlibdir}/geoR/INDEX
%{rlibdir}/geoR/NAMESPACE
%{rlibdir}/geoR/libs
%{rlibdir}/geoR/data
%{rlibdir}/geoR/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.1-1
- initial package for Fedora