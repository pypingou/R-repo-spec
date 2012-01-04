%global packname  mblm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.11
Release:          1%{?dist}
Summary:          Median-Based Linear Models

Group:            Applications/Engineering 
License:          GPL version 2 or newer. http://www.gnu.org/copyleft/gpl.html
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides linear models based on Theil-Sen single median and
Siegel repeated medians. They are very robust (29 or 50 percent breakdown
point, respectively), and if no outliers are present, the estimators are
very similar to OLS.

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
%doc %{rlibdir}/mblm/DESCRIPTION
%doc %{rlibdir}/mblm/html
%{rlibdir}/mblm/Meta
%{rlibdir}/mblm/INDEX
%{rlibdir}/mblm/R
%{rlibdir}/mblm/NAMESPACE
%{rlibdir}/mblm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11-1
- initial package for Fedora