%global packname  compute.es
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Compute Effect Sizes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains several functions for calculating and converting
various statistics, such as a t-test or p-value and sample size, to effect
size estimates of d (mean difference), g (unbiased estimate of d), r
(correlation coefficient), z (Fisher's z), and log odds ratio. The
variance of these estimates are also computed. These
calculation/conversion functions are a particularly useful resource during
the preliminary stages of a meta-analytic project when deriving effect
sizes from reported data. This package uses recommended formulas as
described in The Handbook of Research Synthesis and Meta-Analysis (Cooper,
Hedges, & Valentine, 2009).

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
%doc %{rlibdir}/compute.es/html
%doc %{rlibdir}/compute.es/DESCRIPTION
%{rlibdir}/compute.es/INDEX
%{rlibdir}/compute.es/Meta
%{rlibdir}/compute.es/NAMESPACE
%{rlibdir}/compute.es/help
%{rlibdir}/compute.es/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora