%global packname  CITAN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.08.1
Release:          1%{?dist}
Summary:          CITation ANalysis toolpack

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.08-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-DBI R-RSQLite R-RGtk2 R-hash R-ADGofTest 


BuildRequires:    R-devel tex(latex) R-DBI R-RSQLite R-RGtk2 R-hash R-ADGofTest



%description
CITAN is a library of functions useful in - but not limited to -
quantitative research in the field of scientometrics. It contains various
tools for preprocessing bibliographic data retrieved e.g. from Elsevier's
SciVerse Scopus and calculating bibliometric impact of individuals. Also,
many functions dealing with Pareto-Type II (GPD) and Discretized
Pareto-Type II statistical models are included (e.g. Zhang-Stephens and
MLE estimators, goodness-of-fit and two-sample tests, confidence intervals
for the theoretical Hirsch index etc.). They may be used to describe and
analyze many phenomena encountered in the social sciences.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.08.1-1
- initial package for Fedora