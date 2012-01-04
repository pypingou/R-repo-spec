%global packname  pathClass
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Classification using biological pathways as prior knowledge

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-svmpath R-kernlab R-affy R-Biobase R-ROCR R-igraph R-lpSolve 


BuildRequires:    R-devel tex(latex) R-svmpath R-kernlab R-affy R-Biobase R-ROCR R-igraph R-lpSolve



%description
pathClass is a collection of classification methods that use information
about feature connectivity in a biological network as an additional source
of information. This additional knowledge is incorporated into the
classification a priori. Several authors have shown that this approach
significantly increases the classification performance.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora