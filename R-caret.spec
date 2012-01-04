%global packname  caret
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.09.012
Release:          1%{?dist}
Summary:          Classification and Regression Training

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_5.09-012.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-reshape R-stats R-plyr R-cluster R-foreach 


BuildRequires:    R-devel tex(latex) R-lattice R-reshape R-stats R-plyr R-cluster R-foreach



%description
Misc functions for training and plotting classification and regression

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.09.012-1
- initial package for Fedora