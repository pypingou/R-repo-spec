%global packname  SiZer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          SiZer: Significant Zero Crossings

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines R-boot 

BuildRequires:    R-devel tex(latex) R-splines R-boot 

%description
Calculates and plots the SiZer map for scatterplot data. A SiZer map is a
way of examining when the p-th derivative of a scatterplot-smoother is
significantly negative, possibly zero or significantly positive across a
range of smoothing bandwidths.

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
%doc %{rlibdir}/SiZer/DESCRIPTION
%doc %{rlibdir}/SiZer/html
%{rlibdir}/SiZer/Meta
%{rlibdir}/SiZer/help
%{rlibdir}/SiZer/data
%{rlibdir}/SiZer/INDEX
%{rlibdir}/SiZer/R
%{rlibdir}/SiZer/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora