%global packname  mirf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          MULTIPLE IMPUTATION AND RANDOM FORESTS FOR UNOBSERVABLE PHASE, HIGH-DIMENSIONAL DATA

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-haplo.stats R-randomForest 

BuildRequires:    R-devel tex(latex) R-haplo.stats R-randomForest 

%description
This package applies a combination of missing haplotype imputation via the
EM algorithm of Excoffier and Slatkin(1995) and modelling trait-haplotype
associations via the Random Forest algorithm. The EM algorithm is
implemented by the function haplo.em (of the haplo.stats package) and the
Random Forest algorithm is implemented by the randomForest function (of
the randomForest package). This method is described in the published
manuscript: B.A.S. Nonyane and A.S. Foulkes (2007) Multiple imputation and
random forests (MIRF) for unobservable high-dimensional data. The
International Journal of Biostatistics 3(1): Article 12.

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
%doc %{rlibdir}/mirf/DESCRIPTION
%doc %{rlibdir}/mirf/html
%{rlibdir}/mirf/help
%{rlibdir}/mirf/data
%{rlibdir}/mirf/Meta
%{rlibdir}/mirf/R
%{rlibdir}/mirf/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora