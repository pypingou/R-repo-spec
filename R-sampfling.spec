%global packname  sampfling
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.3.1
Release:          1%{?dist}
Summary:          Sampford sampling (w/o replacement and unequal probabilities)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-3.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implements a modified version of the Sampford sampling algorithm. Given a
quantity assigned to each unit in the population, samples are drawn with
probability proportional to the product of the quantities of the units
included in the sample.

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
%doc %{rlibdir}/sampfling/DESCRIPTION
%doc %{rlibdir}/sampfling/html
%{rlibdir}/sampfling/libs
%{rlibdir}/sampfling/Meta
%{rlibdir}/sampfling/INDEX
%{rlibdir}/sampfling/NAMESPACE
%{rlibdir}/sampfling/help
%{rlibdir}/sampfling/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.3.1-1
- initial package for Fedora