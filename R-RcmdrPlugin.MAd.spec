%global packname  RcmdrPlugin.MAd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Meta-Analysis with Mean Differences (MAd) Rcmdr Plug-in

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-MAd 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-MAd 

%description
This is an R-Commander plug-in for the MAd package (Meta-Analysis with
Mean Differences). This package enables the user to conduct a
meta-analysis in a menu-driven, graphical user interface environment
(e.g., SPSS), while having the full statistical capabilities of R and the
MAd package. The MAd package itself contains a variety of useful functions
for conducting a research synthesis with mean differences data. One of the
unique features of the MAd package is in its integration of user-friendly
functions to complete many of the statistical steps involved in a
meta-analysis with mean differences. It uses recommended procedures as
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
%doc %{rlibdir}/RcmdrPlugin.MAd/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.MAd/html
%{rlibdir}/RcmdrPlugin.MAd/Meta
%{rlibdir}/RcmdrPlugin.MAd/INDEX
%{rlibdir}/RcmdrPlugin.MAd/etc
%{rlibdir}/RcmdrPlugin.MAd/R
%{rlibdir}/RcmdrPlugin.MAd/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora