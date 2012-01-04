%global packname  classifly
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Explore classification models in high dimensions

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rpart R-MASS R-nnet R-class R-e1071 R-reshape 


BuildRequires:    R-devel tex(latex) R-rpart R-MASS R-nnet R-class R-e1071 R-reshape



%description
Given $p$-dimensional training data containing $d$ groups (the design
space), a classification algorithm (classifier) predicts which group new
data belongs to.  Generally the input to these algorithms is high
dimensional, and the boundaries between groups will be high dimensional
and perhaps curvilinear or multi-faceted. This package implements methods
for understanding the division of space between the groups.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora