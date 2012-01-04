%global packname  scagnostics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Compute scagnostics - scatterplot diagnostics

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Calculates graph theoretic scagnostics. Scagnostics describe various
measures of interest for pairs of variables, based on their appearance on
a scatterplot.  They are useful tool for discovering interesting or
unusual scatterplots from a scatterplot matrix, without having to look at
every individual plot.

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
%doc %{rlibdir}/scagnostics/html
%doc %{rlibdir}/scagnostics/DESCRIPTION
%{rlibdir}/scagnostics/INDEX
%{rlibdir}/scagnostics/help
%{rlibdir}/scagnostics/Meta
%{rlibdir}/scagnostics/LICENSE
%{rlibdir}/scagnostics/R
%{rlibdir}/scagnostics/NAMESPACE
%{rlibdir}/scagnostics/java

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora