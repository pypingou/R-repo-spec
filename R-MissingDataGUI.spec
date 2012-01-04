%global packname  MissingDataGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          A GUI for Missing Data Exploration

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gWidgetsRGtk2 R-cairoDevice R-GGally R-Hmisc R-norm 

BuildRequires:    R-devel tex(latex) R-gWidgetsRGtk2 R-cairoDevice R-GGally R-Hmisc R-norm 

%description
This package provides numeric and graphical summaries for the missing
values from both discrete and continuous variables. A variety of
imputation methods are applied, including univariate imputations like
fixed or random values, multiple imputations based on other packages, and
imputations conditioned on a categorical variable.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora