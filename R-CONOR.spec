%global packname  CONOR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          CONOR

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-CLSOCP R-tseries R-outliers R-nortest R-quadprog R-zoo R-preprocessCore R-fields R-fpc R-flexclust R-plyr R-CONORData 

BuildRequires:    R-devel tex(latex) R-CLSOCP R-tseries R-outliers R-nortest R-quadprog R-zoo R-preprocessCore R-fields R-fpc R-flexclust R-plyr R-CONORData 

%description
CrOss-platform NOrmalization in R: normalize gene expression data to be
comparable for different microarray platforms.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora