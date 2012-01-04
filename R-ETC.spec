%global packname  ETC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Equivalence to control

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm 


%description
The package allows selecting those treatments of a one-way layout being
equivalent to a control. Bonferroni adjusted "two one-sided t-tests"
(TOST) and related simultaneous confidence intervals are given for both
differences or ratios of means of normally distributed data. For the case
of equal variances and balanced sample sizes for the treatment groups, the
single-step procedure of Bofinger and Bofinger (1995) can be chosen. For
non-normal data, the Wilcoxon test is applied.

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
%doc %{rlibdir}/ETC/DESCRIPTION
%doc %{rlibdir}/ETC/html
%{rlibdir}/ETC/Meta
%{rlibdir}/ETC/data
%{rlibdir}/ETC/R
%{rlibdir}/ETC/NAMESPACE
%{rlibdir}/ETC/help
%{rlibdir}/ETC/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora