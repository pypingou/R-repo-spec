%global packname  xlsxjars
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Package required jars for the xlsx package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
The xlsxjars package collects all the external jars required for the xlxs
package.  These external jars are quite large in size (15MB) and have a
slow release cycle.  By separating the Java and R development, the storage
footprint on CRAN is reduced. This release corresponds to POI 3.7.

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
%doc %{rlibdir}/xlsxjars/NEWS
%doc %{rlibdir}/xlsxjars/html
%doc %{rlibdir}/xlsxjars/DESCRIPTION
%{rlibdir}/xlsxjars/Meta
%{rlibdir}/xlsxjars/INDEX
%{rlibdir}/xlsxjars/java
%{rlibdir}/xlsxjars/NAMESPACE
%{rlibdir}/xlsxjars/help
%{rlibdir}/xlsxjars/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora