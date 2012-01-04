%global packname  RcmdrPlugin.MAc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Meta-Analysis with Correlations (MAc) Rcmdr Plug-in

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-MAc 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-MAc 

%description
This is an R-Commander plug-in for the MAc package (Meta-Analysis with
Correlations). This package enables the user to conduct a meta-analysis in
a menu-driven, graphical user interface environment (e.g., SPSS), while
having the full statistical capabilities of R and the MAc package. The MAc
package itself contains a variety of useful functions for conducting a
research synthesis with correlational data. One of the unique features of
the MAc package is in its integration of user-friendly functions to
complete the majority of statistical steps involved in a meta-analysis
with correlations. It uses recommended procedures as described in The
Handbook of Research Synthesis and Meta-Analysis (Cooper, Hedges, &
Valentine, 2009).

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
%doc %{rlibdir}/RcmdrPlugin.MAc/html
%doc %{rlibdir}/RcmdrPlugin.MAc/DESCRIPTION
%{rlibdir}/RcmdrPlugin.MAc/INDEX
%{rlibdir}/RcmdrPlugin.MAc/etc
%{rlibdir}/RcmdrPlugin.MAc/R
%{rlibdir}/RcmdrPlugin.MAc/Meta
%{rlibdir}/RcmdrPlugin.MAc/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9-1
- initial package for Fedora