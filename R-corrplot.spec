%global packname  corrplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.40
Release:          1%{?dist}
Summary:          visualization of a correlation matrix

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The corrplot package is a graphical display of a correlation matrix,
confidence interval. It also contains some algorithms to do matrix

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
%doc %{rlibdir}/corrplot/DESCRIPTION
%doc %{rlibdir}/corrplot/html
%{rlibdir}/corrplot/Meta
%{rlibdir}/corrplot/INDEX
%{rlibdir}/corrplot/R
%{rlibdir}/corrplot/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.40-1
- initial package for Fedora