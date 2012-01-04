%global packname  knncat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.11
Release:          1%{?dist}
Summary:          Nearest-neighbor classification with categorical variables

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This program scales categorical variables in such a way as to make NN
classification as accurate as possible. It also handles continuous
variables and prior probabilities, and does intelligent variable selection
and estimation of error rates and the right number of NN's.

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
%doc %{rlibdir}/knncat/DESCRIPTION
%doc %{rlibdir}/knncat/html
%{rlibdir}/knncat/NAMESPACE
%{rlibdir}/knncat/INDEX
%{rlibdir}/knncat/help
%{rlibdir}/knncat/Meta
%{rlibdir}/knncat/R
%{rlibdir}/knncat/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.11-1
- initial package for Fedora