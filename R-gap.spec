%global packname  gap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Genetic analysis package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
It is designed as an integrated package for genetic data analysis of both
population and family data. Currently, it contains functions for sample
size calculations of both population-based and family-based designs,
classic twin models, probability of familial disease aggregation, kinship
calculation, some statistics in linkage analysis, and association analysis
involving one or more genetic markers including haplotype analysis with or
without environmental covariates.

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
%doc %{rlibdir}/gap/DESCRIPTION
%doc %{rlibdir}/gap/doc
%doc %{rlibdir}/gap/html
%{rlibdir}/gap/help
%{rlibdir}/gap/R
%{rlibdir}/gap/demo
%{rlibdir}/gap/klem
%{rlibdir}/gap/data
%{rlibdir}/gap/INDEX
%{rlibdir}/gap/comp.score
%{rlibdir}/gap/OpenMx
%{rlibdir}/gap/tests
%{rlibdir}/gap/NAMESPACE
RPM build errors:
%{rlibdir}/gap/libs
%{rlibdir}/gap/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora