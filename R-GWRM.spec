%global packname  GWRM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          GWRM

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
GWRM is a package for fitting Generalized Waring Regression Models. It
includes the dataset and the example of Rodriguez-Avi, J; Conde-Sanchez,
A; Saez-Castillo, A.J., Olmo-Jimenez, M. J. and Martinez Rodriguez, A.
M.(2009). A generalized Waring regression model for count data.
Computational Statistics and Data Analysis, 53, pp. 3717-3725.

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
%doc %{rlibdir}/GWRM/html
%doc %{rlibdir}/GWRM/DESCRIPTION
%doc %{rlibdir}/GWRM/CITATION
%{rlibdir}/GWRM/data
%{rlibdir}/GWRM/Meta
%{rlibdir}/GWRM/NAMESPACE
%{rlibdir}/GWRM/INDEX
%{rlibdir}/GWRM/R
%{rlibdir}/GWRM/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora