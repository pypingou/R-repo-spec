%global packname  mcga
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Machine coded genetic algorihms for real-valued optimization problems

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Machine coded genetic algorithm (MCGA) is a fast tool for real-valued
optimization problems. It uses the byte representation of variables rather
than real-values. It performs the classical crossover operations (uniform)
on these byte representations. Mutation operator is also similar to
classical mutation operator, which is to say, it changes a randomly
selected byte value of a chromosome by +1 or -1 with probability 1/2. In
MCGAs there is no need for encoding-decoding process and the classical
operators are directly applicable on real-values. It is fast and can
handle a wide range of a search space with high precision. Using a
256-unary alphabet is the main disadvantage of this algorithm but a
moderate size population is convenient for many problems.

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
%doc %{rlibdir}/mcga/html
%doc %{rlibdir}/mcga/DESCRIPTION
%{rlibdir}/mcga/NAMESPACE
%{rlibdir}/mcga/INDEX
%{rlibdir}/mcga/R
%{rlibdir}/mcga/help
%{rlibdir}/mcga/libs
%{rlibdir}/mcga/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora