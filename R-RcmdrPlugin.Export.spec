%global packname  RcmdrPlugin.Export
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Graphically export output to LaTeX or HTML

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-xtable R-Hmisc 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-xtable R-Hmisc 

%description
The package helps users to graphically export Rcmdr output to LaTeX or
HTML code, via xtable() or Hmisc::latex(). The plug-in was originally
intended to facilitate exporting Rcmdr output to formats other than ASCII
text and to provide R novices with an easy-to-use, easy-to-access
reference on exporting R objects to formats suited for printed output. The
package documentation contains several pointers on creating reports,
either by using conventional word processors or LaTeX/LyX.

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
%doc %{rlibdir}/RcmdrPlugin.Export/html
%doc %{rlibdir}/RcmdrPlugin.Export/DESCRIPTION
%{rlibdir}/RcmdrPlugin.Export/LIMITATIONS
%{rlibdir}/RcmdrPlugin.Export/ChangeLog
%{rlibdir}/RcmdrPlugin.Export/INDEX
%{rlibdir}/RcmdrPlugin.Export/etc
%{rlibdir}/RcmdrPlugin.Export/help
%{rlibdir}/RcmdrPlugin.Export/Meta
%{rlibdir}/RcmdrPlugin.Export/R

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora