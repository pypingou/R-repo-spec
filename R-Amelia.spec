%global packname  Amelia
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Amelia II: A Program for Missing Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreign R-utils 

BuildRequires:    R-devel tex(latex) R-foreign R-utils 

%description
Amelia II "multiply imputes" missing data in a single cross-section (such
as a survey), from a time series (like variables collected for each year
in a country), or from a time-series-cross-sectional data set (such as
collected by years for each of several countries). Amelia II implements
our bootstrapping-based algorithm that gives essentially the same answers
as the standard IP or EMis approaches, is usually considerably faster than
existing approaches and can handle many more variables.  Unlike Amelia I
and other statistically rigorous imputation software, it virtually never
crashes (but please let us know if you find to the contrary!).  The
program also generalizes existing approaches by allowing for trends in
time series across observations within a cross-sectional unit, as well as
priors that allow experts to incorporate beliefs they have about the
values of missing cells in their data. Amelia II also includes useful
diagnostics of the fit of multiple imputation models.  The program works
from the R command line or via a graphical user interface that does not
require users to know R.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.4-1
- initial package for Fedora