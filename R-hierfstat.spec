%global packname  hierfstat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.04.6
Release:          1%{?dist}
Summary:          Estimation and tests of hierarchical F-statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.04-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gtools 


BuildRequires:    R-devel tex(latex) R-gtools



%description
This R package allows the estimation of hierarchical F-statistics from
haploid or diploid genetic data with any numbers of levels in the
hierarchy, following the algorithm of Yang (Evolution, 1998,
52(4):950-956). Functions are also given to test via randomisations the
significance of each F and variance components, using the likelihood-ratio
statistics G -see Goudet etal (Genetics, 1996, 144(4): 1933-1940)

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
%doc %{rlibdir}/hierfstat/DESCRIPTION
%doc %{rlibdir}/hierfstat/doc
%doc %{rlibdir}/hierfstat/html
%{rlibdir}/hierfstat/R
%{rlibdir}/hierfstat/INDEX
%{rlibdir}/hierfstat/extdata
%{rlibdir}/hierfstat/NAMESPACE
%{rlibdir}/hierfstat/Meta
%{rlibdir}/hierfstat/data
%{rlibdir}/hierfstat/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.04.6-1
- initial package for Fedora