%global packname  knnflex
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          A more flexible KNN

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A KNN implementaion which allows continuous responses, the specification
of the distance used to calculate nearest neighbors (euclidean, binary,
etc.), the aggregation method used to summarize repsonse (majority class,
mean, etc.) and the method of handling ties (all, random selection, etc.).

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
%doc %{rlibdir}/knnflex/html
%doc %{rlibdir}/knnflex/DESCRIPTION
%{rlibdir}/knnflex/INDEX
%{rlibdir}/knnflex/Meta
%{rlibdir}/knnflex/R
%{rlibdir}/knnflex/NAMESPACE
%{rlibdir}/knnflex/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora