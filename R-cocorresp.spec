%global packname  cocorresp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Co-correspondence analysis methods

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics R-vegan 


BuildRequires:    R-devel tex(latex) R-stats R-graphics R-vegan



%description
Fits predictive and symmetric co-correspondence analysis (CoCA) models to
relate one data matrix to another data matrix. More specifically, CoCA
maximises the weighted covariance between the weighted averaged species
scores of one community and the weighted averaged species scores of
another community. CoCA attempts to find patterns that are common to both

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.9-1
- initial package for Fedora