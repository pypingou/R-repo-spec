%global packname  DAAG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.08
Release:          1%{?dist}
Summary:          Data Analysis And Graphics data and functions

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-rpart R-randomForest R-boot R-nlme R-survival 


BuildRequires:    R-devel tex(latex) R-MASS R-rpart R-randomForest R-boot R-nlme R-survival



%description
various data sets used in examples and exercises in the book Maindonald,
J.H. and Braun, W.J. (2003, 2007, 2010) "Data Analysis and Graphics Using

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
%doc %{rlibdir}/DAAG/doc
%doc %{rlibdir}/DAAG/html
%doc %{rlibdir}/DAAG/DESCRIPTION
%{rlibdir}/DAAG/INDEX
%{rlibdir}/DAAG/seedrates.txt
%{rlibdir}/DAAG/help
%{rlibdir}/DAAG/NAMESPACE
%{rlibdir}/DAAG/misc
%{rlibdir}/DAAG/R
%{rlibdir}/DAAG/Meta
%{rlibdir}/DAAG/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.08-1
- initial package for Fedora