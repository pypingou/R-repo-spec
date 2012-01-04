%global packname  digeR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          GUI tool for analyzing 2D DIGE data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gWidgets R-MASS R-pls R-e1071 R-adabag R-randomForest R-ROCR R-caTools R-class R-ellipse 


BuildRequires:    R-devel tex(latex) R-gWidgets R-MASS R-pls R-e1071 R-adabag R-randomForest R-ROCR R-caTools R-class R-ellipse



%description
An easy to use Graphical User Interfact for spots correlation analysis,
score plot, classification, feature selection and power analysis for 2D
DIGE experiment data.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora