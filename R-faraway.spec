%global packname  faraway
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Functions and datasets for books by Julian Faraway.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Books are "Practical Regression and ANOVA in R" on CRAN, "Linear Models
with R" published in August 2004 by CRC press and "Extending the Linear
Model with R" published by CRC press in December 2005.

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
%doc %{rlibdir}/faraway/DESCRIPTION
%doc %{rlibdir}/faraway/html
%{rlibdir}/faraway/help
%{rlibdir}/faraway/NAMESPACE
%{rlibdir}/faraway/INDEX
%{rlibdir}/faraway/Meta
%{rlibdir}/faraway/R
%{rlibdir}/faraway/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora