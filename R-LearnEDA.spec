%global packname  LearnEDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          Functions for Learning Exploratory Data Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
LearnEDA contains a collection of functions helpful in learning the basic
tenets of Exploratory Data Analysis.

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
%doc %{rlibdir}/LearnEDA/html
%doc %{rlibdir}/LearnEDA/DESCRIPTION
%{rlibdir}/LearnEDA/R
%{rlibdir}/LearnEDA/INDEX
%{rlibdir}/LearnEDA/NAMESPACE
%{rlibdir}/LearnEDA/help
%{rlibdir}/LearnEDA/Meta
%{rlibdir}/LearnEDA/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora