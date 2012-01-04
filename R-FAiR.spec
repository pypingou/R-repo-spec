%global packname  FAiR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.7
Release:          1%{?dist}
Summary:          Factor Analysis in R

Group:            Applications/Engineering 
License:          AGPL (>= 3) + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-rgenoud R-gWidgetsRGtk2 R-stats4 R-rrcov R-Matrix 
Requires:         R-stats4 R-rrcov 

BuildRequires:    R-devel tex(latex) R-methods R-rgenoud R-gWidgetsRGtk2 R-stats4 R-rrcov R-Matrix
BuildRequires:    R-stats4 R-rrcov 


%description
This package estimates factor analysis models using a genetic algorithm,
which permits a general mechanism for restricted optimization with
arbitrary restrictions that are chosen at run time with the help of a GUI.
Importantly, inequality restrictions can be imposed on functions of
multiple parameters, which provides a new avenues for testing and
generating theories with factor analysis models. This package also
includes an entirely new estimator of the common factor analysis model
called semi-exploratory factor analysis, which is a general alternative to
exploratory and confirmatory factor analysis. Finally, this package
integrates a lot of other packages that estimate sample covariance
matrices and thus provides a lot of alternatives to the traditional sample
covariance calculation. Note that you need to have the Gtk run time
library installed on your system to use this package; see the URL below
for detailed installation instructions. Most users would only need to
understand the first twenty-four pages of the PDF manual.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.7-1
- initial package for Fedora