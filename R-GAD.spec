%global packname  GAD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          GAD: Analysis of variance from general principles

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-matrixStats R-R.methodsS3 

BuildRequires:    R-devel tex(latex) R-stats R-matrixStats R-R.methodsS3 

%description
This package analyses complex ANOVA models with any combination of
orthogonal/nested and fixed/random factors, as described by Underwood
(1997). There are two restrictions: (i) data must be balanced; (ii) fixed
nested factors are not allowed. Homogeneity of variances is checked using
Cochran's C test and 'a posteriori' comparisons of means are done using
Student-Newman-Keuls (SNK) procedure.

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
%doc %{rlibdir}/GAD/html
%doc %{rlibdir}/GAD/CITATION
%doc %{rlibdir}/GAD/DESCRIPTION
%{rlibdir}/GAD/INDEX
%{rlibdir}/GAD/Meta
%{rlibdir}/GAD/data
%{rlibdir}/GAD/help
%{rlibdir}/GAD/R

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora